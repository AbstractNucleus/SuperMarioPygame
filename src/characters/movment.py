def movment_y(pygame,keys,y):
    if keys[pygame.K_w] or keys[pygame.K_SPACE] or  keys[pygame.K_UP]:
        y -= 5
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        y += 5
    return y

def movment_x(pygame,keys,x):
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        x -= 5
    return x