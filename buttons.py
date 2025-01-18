import pygame as pg

def draw_button(screen, rect, text, rect_color, color, btn_width, font, image_path = None):
    pg.draw.rect(screen, rect_color, rect, btn_width)

    if image_path:
        button_image = pg.image.load(image_path)
        image_rect = button_image.get_rect(center = (rect[0]+ rect.width//2, rect[1] + rect.height//2))
        screen.blit(button_image, image_rect)

    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(rect[0]+rect.width//2, rect[1]+rect.height//2))
    screen.blit(text_surface, text_rect)