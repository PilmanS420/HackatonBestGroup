from classes.Button import Button
import pygame


def stage1():
    global current_stage
    """
    stage settings
    
    """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_stage = "exit"
                return None


def stage_start():
    global current_stage
    """
    stage settings

    """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_stage = "exit"
                return None


# Main function to manage stages
def main():
    global current_stage
    # Setting up pygame window
    pygame.init()
    pygame.display.set_caption("Ur Mom")

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # Game stages loop
    while current_stage != "exit":
        if current_stage == "start":
            stage_start()
        elif current_stage == "stage1":
            stage1()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    current_stage = "start"  # A variable keep current activity name to manage game screens
    main()
