# 
# Algoritms Visualizer
# Try oang
#
from algorithms import Algos
import pygame, random
pygame.init()
class Construct:
    """ Constructor
    
    Build the window, and contain the visualize list
    """
    width = 800
    height = 600
    NEON_YELLOW = 224,231,34
    NEON_BLUE = 77, 77, 255
    NEON_GREEN = 68,214,44
    BAR_COLOR = 254,254,254
    HORIZONTAL_PAD = width*.1
    VERTICAL_PAD = height*.2
    FONT = pygame.font.SysFont('Lucida Sans', 17)
    FONTS = pygame.font.SysFont('Lucida Sans', 14)

    def __init__(self, arr,width=800, height=600):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(f"Algo Visualizer | ")
        self.set_list(arr)
    # Setting the list
    # then computing the length of each bar, to fit in specified width and height
    def set_list(self, arr):
        self.arr = arr
        self.min_val = min(arr)
        self.max_val = max(arr)

        self.section_width = round((self.width-self.HORIZONTAL_PAD) / len(arr))
        self.section_height = round((self.height-self.VERTICAL_PAD) / (self.max_val - self.min_val))
        self.start_x = self.HORIZONTAL_PAD //2
    # Set the algo
    def set_algo(self,algo):
        self.algo = algo
        pygame.display.set_caption(f"Algo Visualizer | {algo}")
    def construct_list_values(self, color_sel={}, clear_b=False):
        arr = self.arr
        if clear_b:
            clear_rect = (self.start_x, self.VERTICAL_PAD,
                self.width - self.HORIZONTAL_PAD, self.height-self.VERTICAL_PAD)
            pygame.draw.rect(self.window, (0,0,0),clear_rect)
        for i, v in enumerate(arr):
            x = self.start_x + (i) * self.section_width
            y = (self.height // 2) + self.section_height

            if i in color_sel:
                pygame.draw.rect(self.window,color_sel[i],(x, y, self.section_width, self.section_height*4))
                self.window.blit(self.FONTS.render(f'{v}', True, (0,0,0)), (x, y))
            else:
                pygame.draw.rect(self.window,self.BAR_COLOR,(x, y, self.section_width, self.section_height*4))
                self.window.blit(self.FONTS.render(f'{v}', True, (0,0,0)), (x, y))

        if clear_b:
            pygame.display.update()
    def get_random(self):
        val = random.choice(self.arr)
        return val
    def set_target(self, target, clear_b=False):
        sorting = self.FONT.render(f"Find: {target}", 1, (self.BAR_COLOR))
        if clear_b:
            clear_rect = ((self.width//2 - sorting.get_width()//2) , 5*10, sorting.get_width(), sorting.get_height())
            pygame.draw.rect(self.window, (0,0,0),clear_rect)
        self.window.blit(sorting, ((self.width//2 - sorting.get_width()//2) , 5*10))
        if clear_b:
            pygame.display.update()
    # Function to visualize the value from the list
    def construct_list_bar(self, color_sel={},clear_b=False):
        arr = self.arr

        if clear_b:
            clear_rect = (self.start_x, self.VERTICAL_PAD,
                self.width - self.HORIZONTAL_PAD, self.height-self.VERTICAL_PAD)
            pygame.draw.rect(self.window, (0,0,0),clear_rect)


        for i, v in enumerate(arr):
            x = self.start_x + (i) * self.section_width
            y = self.height - (v-self.min_val) * self.section_height
            xs = self.start_x + (i+(.25)) * self.section_width

            if i in color_sel:
                pygame.draw.rect(self.window,color_sel[i],(xs, y, self.section_width, self.height*.8))
            else:
                pygame.draw.rect(self.window,self.NEON_BLUE,(x, y, self.section_width, self.height*.8))
                pygame.draw.rect(self.window,self.BAR_COLOR,(xs, y+2, self.section_width*.7, self.height*.8))
        if clear_b:
            pygame.display.update()


def draw1(construct):
    controls = construct.FONT.render("| SPACE - Start Sort | R - Reset | ", 1, (construct.BAR_COLOR))
    construct.window.blit(controls, ((construct.width//2 - controls.get_width()//2) , 5))
    sorting = construct.FONT.render("| 1 = Bubble Sort | 2 = Insertion Sort | 3 = Comb Sort |", 1, (construct.BAR_COLOR))
    construct.window.blit(sorting, ((construct.width//2 - sorting.get_width()//2) , 5*5))
    order = construct.FONT.render("| A = Ascending(Default) | D = Descending|", 1, (construct.NEON_BLUE))
    construct.window.blit(order, ((construct.width//2 - order.get_width()//2) , 5*9))
    construct.construct_list_bar(clear_b=True)
    pygame.display.update()
def draw2(construct, count):
    controls = construct.FONT.render("| SPACE - Start Search | R - Reset | ", 1, (construct.BAR_COLOR))
    construct.window.blit(controls, ((construct.width//2 - controls.get_width()//2) , 5))
    sorting = construct.FONT.render("| 1 = Linear Search | 2 = Binary Search |", 1, (construct.BAR_COLOR))
    construct.window.blit(sorting, ((construct.width//2 - sorting.get_width()//2) , 5*5))
    if count != -1:
        construct.construct_list_values({count:construct.NEON_GREEN}, True)
    else:
        construct.construct_list_values()

        
    pygame.display.update()


# Generate random list
def generate_random_list(n, maxVal, minVal):
    lists = []
    for _ in range(n):
        val = random.randint(minVal, maxVal)
        lists.append(val)
    return lists
# main function or event loop
def main1():
    clock = pygame.time.Clock()
    run = True

    n = 50
    max_v = 100
    min_val = 2
    lis1 = generate_random_list(n, max_v, min_val)
    construct = Construct(lis1)
    sorting = False
    ascending = True
    algorithms = Algos(construct)
    sorting_algo_generator = None

    while run:
        clock.tick(20)
        construct.construct_list_bar()
        if sorting:
            try:
                next(sorting_algo_generator)
            except StopIteration:
                sorting = False
        else:
            draw1(construct)
        # Event Checker
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if not sorting:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        sorting_algo = algorithms.bubble_sort
                        construct.set_algo("Bubble Sort")
                    if event.key == pygame.K_2:
                        construct.set_algo("Insertion Sort")
                        
                        sorting_algo = algorithms.insertion_sort
                    if event.key == pygame.K_3:
                        construct.set_algo("Comb Sort")
                        sorting_algo = algorithms.comb_sort

                    if  event.key == pygame.K_r:
                        lis1 = generate_random_list(n, max_v, min_val)
                        construct.set_list(lis1)
                        algorithms.set_list(lis1)
                        sorting = False
                    if event.key == pygame.K_SPACE and sorting == False:
                        sorting = True
                        sorting_algo_generator = sorting_algo(ascending)
                        
                    elif event.key ==  pygame.K_d :
                        ascending = False
                    elif event.key == pygame.K_a :
                        ascending = True
    pygame.quit()
    
def main2():
    clock = pygame.time.Clock()
    run = True

    n = 30
    max_v = 100
    min_val = 2
    lis1 = generate_random_list(n, max_v, min_val)
    construct = Construct(lis1)
    searching = False
    
    algorithms = Algos(construct)
    searching_algo_generator = None
    val = construct.get_random()
    algorithms.set_target(val)
    construct.set_target(val)
    
    
    count = -1
    pressed = False
    while run:
        clock.tick(10)
        construct.construct_list_values()
        if searching:
            try:
                count = next(searching_algo_generator)
                
            except StopIteration:
                searching = False
        else:
            draw2(construct, count)
        # Event Checker
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if not searching:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        searching_algo = algorithms.linear_search
                        construct.set_algo("Linear Search")
                        pressed = True
                        
                        
                    if event.key == pygame.K_2:
                        construct.set_algo("Binary Search")
                        lis1 = sorted(construct.arr)
                        
                        construct.set_list(lis1)
                        algorithms.set_list(lis1)
                        searching_algo = algorithms.binary_search
                        pressed = True
                    if  event.key == pygame.K_r:
                        lis1 = generate_random_list(n, max_v, min_val)
                        if construct.algo is ("Binary Search"):
                            lis1 = sorted(lis1)
                        construct.set_list(lis1)
                        algorithms.set_list(lis1)
                        val = construct.get_random()
                        construct.set_target(val, True)
                        algorithms.set_target(val)
                        searching = False
                        count = -1
                    
                    if event.key == pygame.K_SPACE and not searching and pressed:
                        searching = True
                        searching_algo_generator = searching_algo()
                        count = -1


    pygame.quit()
def ex():
    choose = int(input("What Algorithm: (0 = Sorting,  1 = Search): "))
    if choose == 0:
        main1()
    elif choose == 1:
        main2()
    else:
        print("Try Again")
        ex()
if __name__ == "__main__":
    ex()