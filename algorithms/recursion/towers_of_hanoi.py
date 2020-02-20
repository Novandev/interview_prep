"""
Tower of Hanoi problem

You start off with 3 poles and one of the poles has rings increasing in size in a stack from top to bottom

"""



def tower_of_hanoi_solver(counter: int,start: int, goal: int, temp: int):
    if counter >= 1:
        return tower_of_hanoi_solver(counter-1,start,temp,goal)
        print(f'move {start} => {goal}')
        return tower_of_hanoi_solver(counter-1,temp,goal,start)