
import sys
import pygame
import random

'''滑雪者類'''
class SkierClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # 滑雪者的朝向(-2到2)
        self.direction = 0
        self.imagepaths = cfg.SKIER_IMAGE_PATHS[:-1]
        self.image = pygame.image.load(self.imagepaths[self.direction])
        self.rect = self.image.get_rect()
        self.rect.center = [320, 100]
        self.speed = [self.direction, 6-abs(self.direction)*2]
    '''改變滑雪者的朝向. 負數為向左，正數為向右，0為向前'''
    def turn(self, num):
        self.direction += num
        self.direction = max(-2, self.direction)
        self.direction = min(2, self.direction)
        center = self.rect.center
        self.image = pygame.image.load(self.imagepaths[self.direction])
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed = [self.direction, 6-abs(self.direction)*2]
        return self.speed
    '''移動滑雪者'''
    def move(self):
        self.rect.centerx += self.speed[0]
        self.rect.centerx = max(20, self.rect.centerx)
        self.rect.centerx = min(620, self.rect.centerx)
    '''設置為摔倒狀態'''
    def setFall(self):
        self.image = pygame.image.load(cfg.SKIER_IMAGE_PATHS[-1])
    '''設置為站立狀態'''
    def setForward(self):
        self.direction = 0
        self.image = pygame.image.load(self.imagepaths[self.direction])


'''
Function:
    障礙物類
Input:
    img_path: 障礙物圖片路徑
    location: 障礙物位置
    attribute: 障礙物類別屬性
'''
class ObstacleClass(pygame.sprite.Sprite):
    def __init__(self, img_path, location, attribute):
        pygame.sprite.Sprite.__init__(self)
        self.img_path = img_path
        self.image = pygame.image.load(self.img_path)
        self.location = location
        self.rect = self.image.get_rect()
        self.rect.center = self.location
        self.attribute = attribute
        self.passed = False
    '''移動'''
    def move(self, num):
        self.rect.centery = self.location[1] - num


'''創建障礙物'''
def createObstacles(s, e, num=10):
    obstacles = pygame.sprite.Group()
    locations = []
    for i in range(num):
        row = random.randint(s, e)
        col = random.randint(0, 9)
        location  = [col*64+20, row*64+20]
        if location not in locations:
            locations.append(location)
            attribute = random.choice(list(cfg.OBSTACLE_PATHS.keys()))
            img_path = cfg.OBSTACLE_PATHS[attribute]
            obstacle = ObstacleClass(img_path, location, attribute)
            obstacles.add(obstacle)
    return obstacles


'''合併障礙物'''
def AddObstacles(obstacles0, obstacles1):
    obstacles = pygame.sprite.Group()
    for obstacle in obstacles0:
        obstacles.add(obstacle)
    for obstacle in obstacles1:
        obstacles.add(obstacle)
    return obstacles


'''顯示遊戲開始界面'''
def ShowStartInterface(screen, screensize):
    screen.fill((255, 255, 255))
    tfont = pygame.font.Font(cfg.FONTPATH, screensize[0]//5)
    cfont = pygame.font.Font(cfg.FONTPATH, screensize[0]//20)
    title = tfont.render(u'滑雪遊戲', True, (255, 0, 0))
    content = cfont.render(u'按任意鍵開始遊戲', True, (0, 0, 255))
    trect = title.get_rect()
    trect.midtop = (screensize[0]/2, screensize[1]/5)
    crect = content.get_rect()
    crect.midtop = (screensize[0]/2, screensize[1]/2)
    screen.blit(title, trect)
    screen.blit(content, crect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                return
        pygame.display.update()


'''顯示分數'''
def showScore(screen, score, pos=(10, 10)):
    font = pygame.font.Font(cfg.FONTPATH, 30)
    score_text = font.render("Score: %s" % score, True, (0, 0, 0))
    screen.blit(score_text, pos)


'''更新當前幀的遊戲畫面'''
def updateFrame(screen, obstacles, skier, score):
    screen.fill((255, 255, 255))
    obstacles.draw(screen)
    screen.blit(skier.image, skier.rect)
    showScore(screen, score)
    pygame.display.update()


'''主程序'''
def main():
    # 遊戲初始化
    pygame.init()
    pygame.mixer.init()
    # pygame.mixer.music.load(cfg.BGMPATH)
    # pygame.mixer.music.set_volume(0.4)
    # pygame.mixer.music.play(-1)
    # 設置屏幕
    screen = pygame.display.set_mode(cfg.SCREENSIZE)
    pygame.display.set_caption('滑雪遊戲 —— 九歌')
    # 遊戲開始界面
    ShowStartInterface(screen, cfg.SCREENSIZE)
    # 實例化遊戲精靈
    # --滑雪者
    skier = SkierClass()
    # --創建障礙物
    obstacles0 = createObstacles(20, 29)
    obstacles1 = createObstacles(10, 19)
    obstaclesflag = 0
    obstacles = AddObstacles(obstacles0, obstacles1)
    # 遊戲clock
    clock = pygame.time.Clock()
    # 記錄滑雪的距離
    distance = 0
    # 記錄當前的分數
    score = 0
    # 記錄當前的速度
    speed = [0, 6]
    # 遊戲主循環
    while True:
        # --事件捕獲
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    speed = skier.turn(-1)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    speed = skier.turn(1)
        # --更新當前遊戲幀的數據
        skier.move()
        distance += speed[1]
        if distance >= 640 and obstaclesflag == 0:
            obstaclesflag = 1
            obstacles0 = createObstacles(20, 29)
            obstacles = AddObstacles(obstacles0, obstacles1)
        if distance >= 1280 and obstaclesflag == 1:
            obstaclesflag = 0
            distance -= 1280
            for obstacle in obstacles0:
                obstacle.location[1] = obstacle.location[1] - 1280
            obstacles1 = createObstacles(10, 19)
            obstacles = AddObstacles(obstacles0, obstacles1)
        for obstacle in obstacles:
            obstacle.move(distance)
        # --碰撞檢測
        hitted_obstacles = pygame.sprite.spritecollide(skier, obstacles, False)
        if hitted_obstacles:
            if hitted_obstacles[0].attribute == "tree" and not hitted_obstacles[0].passed:
                score -= 50
                skier.setFall()
                updateFrame(screen, obstacles, skier, score)
                pygame.time.delay(1000)
                skier.setForward()
                speed = [0, 6]
                hitted_obstacles[0].passed = True
            elif hitted_obstacles[0].attribute == "flag" and not hitted_obstacles[0].passed:
                score += 10
                obstacles.remove(hitted_obstacles[0])
        # --更新屏幕
        updateFrame(screen, obstacles, skier, score)
        clock.tick(cfg.FPS)


'''run'''
if __name__ == '__main__':
    main()