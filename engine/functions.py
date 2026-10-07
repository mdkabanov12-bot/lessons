import math
import pygame

NEAR_PLANE = 0.1
DEFAULT_FOV = 90

def to_radians(degrees):
    return degrees * math.pi / 180.0

def project_point(x, y, z, cam_x, cam_y, cam_z, cam_yaw, cam_pitch, fov, width, height):
    # Перевод точки в локальную систему камеры и поворот по осям
    dx = x - cam_x
    dy = y - cam_y
    dz = z - cam_z

    cos_yaw = math.cos(cam_yaw)
    sin_yaw = math.sin(cam_yaw)
    rx = dx * cos_yaw + dz * sin_yaw
    rz = -dx * sin_yaw + dz * cos_yaw

    cos_pitch = math.cos(cam_pitch)
    sin_pitch = math.sin(cam_pitch)
    ry = dy * cos_pitch - rz * sin_pitch
    final_z = dy * sin_pitch + rz * cos_pitch

    if final_z <= NEAR_PLANE:
       return None

    # Перспективная проекция
    fov_rad = to_radians(fov)
    scale = (width / 2) / math.tan(fov_rad / 2)
    try:
        proj_x = (rx * scale) / final_z
        proj_y = (ry * scale) / final_z
    except:
        return None

    screen_x = width // 2 + int(proj_x)
    screen_y = height // 2 - int(proj_y)

    return screen_x, screen_y, final_z

def draw_filled_triangle(screen, points_2d, color):
    if len(points_2d) < 3:
        return

    # Сортировка вершин по Y для растеризации сверху вниз
    pts = sorted(points_2d, key=lambda k: k[1])
    p1, p2, p3 = pts[0], pts[1], pts[2]
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    def interpolate(y_start, y_end, x_start, x_end):
        if y_end == y_start:
            return []
        slope = (x_end - x_start) / (y_end - y_start)
        xs = []
        for y in range(int(y_start), int(y_end)):
            x = x_start + (y - y_start) * slope
            xs.append(x)
        return xs

    # Вычисление границ треугольника по строкам
    left_xs = interpolate(y1, y3, x1, x3)
    right_xs_top = interpolate(y1, y2, x1, x2)
    right_xs_bottom = interpolate(y2, y3, x2, x3)
    right_xs = right_xs_top + right_xs_bottom

    # Заливка горизонтальными линиями
    for i in range(len(left_xs)):
        if i >= len(right_xs):
            break
        x_left = int(left_xs[i])
        x_right = int(right_xs[i])
        y_current = y1 + i
        
        if x_left > x_right:
            x_left, x_right = x_right, x_left
            
        width_rect = max(1, x_right - x_left)
        pygame.draw.rect(screen, color, (x_left, y_current, width_rect, 1))

def prepare_mesh_faces(vertices, indices, colors=None):
    """Преобразует сырые вершины и индексы в список словарей для рендера."""
    faces_data = []
    color_count = len(colors) if colors else 0
    
    for i, face_idx in enumerate(indices):
        v1 = vertices[face_idx[0]]
        v2 = vertices[face_idx[1]]
        v3 = vertices[face_idx[2]]
        
        color = None
        if colors:
            color = colors[i % color_count]
        else:
            color = (255, 255, 255)
            
        faces_data.append({
            'verts': [v1, v2, v3],
            'color': color
        })
    return faces_data

def render_mesh(screen, faces_data, camera, width, height, fov=DEFAULT_FOV):
    """Сортирует, проецирует и рисует все грани модели."""
    # Сортировка граней по расстоянию до центра (дальние рисуются первыми)
    sorted_faces = sorted(
        faces_data, 
        key=lambda f: math.sqrt(
            ((f['verts'][0][0] + f['verts'][1][0] + f['verts'][2][0])/3 - camera.position[0])**2 +
            ((f['verts'][0][1] + f['verts'][1][1] + f['verts'][2][1])/3 - camera.position[1])**2 +
            ((f['verts'][0][2] + f['verts'][1][2] + f['verts'][2][2])/3 - camera.position[2])**2
        ),
        reverse=True
    )

    drawn_count = 0
    cam_pos = camera.position
    cam_rot = camera.rotation

    for face in sorted_faces:
        v1, v2, v3 = face['verts']
        
        p1 = project_point(v1[0], v1[1], v1[2], *cam_pos, *cam_rot, fov, width, height)
        p2 = project_point(v2[0], v2[1], v2[2], *cam_pos, *cam_rot, fov, width, height)
        p3 = project_point(v3[0], v3[1], v3[2], *cam_pos, *cam_rot, fov, width, height)

        # Рисуем только если все три точки видимы
        if p1 and p2 and p3:
            draw_filled_triangle(screen, [p1[:2], p2[:2], p3[:2]], face['color'])
            drawn_count += 1
            
    return drawn_count
