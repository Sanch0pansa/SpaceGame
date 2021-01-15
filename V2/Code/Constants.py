import json


# Экран
BACKGROUND_COLOR = (42, 18, 148)
SIZE = 1500, 900
CAM_SIZE = SIZE

# Частота кадров
FPS = 65
REAL_FPS = 65

# Ускорение игры
ACCELERATION = 1

# Параметры ИИ
MIN_DIST_TO_OBJECTS = 600
MAX_DIST_TO_ENEMY = 1200
MIN_BULLET_ANGLE = 20
MIN_AIR_ATTACK_HEIGHT = 1600

# Данные
file = open("Data/Skills.json", "r", encoding="utf-8")
skills_data = json.load(file)
file = open("Data/Guns.json", "r", encoding="utf-8")
guns_data = json.load(file)
file = open("Data/Ships.json", "r", encoding="utf-8")
ships_data = json.load(file)
frames_tree2 = {
    "main": {
        "frames": [["./Assets/Images/Bullets/Bullet1.png", 20]],
        "next": "main"
    }
}

# Параметры урона
HIT_DAMAGE_COEFFICIENT = 3

# Графика
LASER_COLOR = (255, 255, 200)
LASER_OUTER_LAYER_COLOR = (255, 174, 0)
LASER_MAX_LENGTH = 12000

EXPL_CENTER_COLOR = (242, 250, 255)
EXPL_SECOND_COLOR = (255, 236, 0)
EXPL_THIRD_COLOR = (255, 170, 0)

# Интерфейс
HEALTH_BAR_WIDTH = 100
HEALTH_BAR_HEIGHT = 20
HEALTH_BAR_MIN_WIDTH = 50
HEALTH_BAR_MIN_HEIGHT = 10
HEALTH_BAR_BORDER_RADIUS = 6
HEALTH_BAR_BACKGROUND = (158, 2, 2)
HEALTH_BAR_COLOR = (0, 232, 131)

SKILL_TILE_SIZE = 60
SKILL_TILE_PADDING = 10
SKILL_BACKGROUND = (102, 102, 102)
SKILL_BACKGROUND_ACTIVE = (140, 140, 140)
SKILL_BACKGROUND_PASSIVE = (90, 150, 150)
SKILL_BORDER_COLOR = (200, 200, 200)
SKILL_BORDER_COLOR_PASSIVE = (140, 255, 255)
SKILL_BORDER_WIDTH = 2
SKILL_BAR_MARGIN = 4
SKILL_BAR_HEIGHT = 10
SKILL_RECHARGE_BAR_BACKGROUND = (54, 54, 54)
SKILL_RECHARGE_BAR_COLOR = (94, 239, 255)
SKILL_USING_BAR_BACKGROUND = (54, 54, 54)
SKILL_USING_BAR_COLOR = (94, 255, 161)
