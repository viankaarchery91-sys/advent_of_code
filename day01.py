
with open("day01.txt", "r") as f:
    rotations: list[str] = f.readlines()



def get_password(rotations: list[str]) -> tuple[int, int]:
    position: int = 50                        # Starting position
    zero_point: int = 0                       # Counter for times landed on 0
    for rotation in rotations:
        direction: str = rotation[0]           # Get the direction (L or R)
        amount: int = int(rotation[1:])        # Get the amount to rotate

        if direction == "L":
            position = (position - amount) % 100           # Wrap around using modulo 100
        elif direction == "R":
            position = (position + amount) % 100
        
        if position == 0:
            zero_point +=1
    return zero_point, position

def get_password_p2(rotations: list[str]) -> tuple[int, int]:
    position: int = 50                        # Starting position
    zero_crossings: int = 0                       # Counter for times landed on 0
    for rotation in rotations:
        direction: str = rotation[0]           # Get the direction (L or R)
        amount: int = int(rotation[1:]) 
        
        zero_crossings += amount // 100
        # remainder_distance: int = amount % 100  
        
        old_position: int = position     # Get the amount to rotate

        if direction == "L":
            position = (position - amount) % 100           # Wrap around using modulo 100
        elif direction == "R":
            position = (position + amount) % 100
        
        if position != 0:
            if direction == "L":
                if (position > old_position) and (old_position != 0):
                    zero_crossings += 1
            if direction == "R":
                if position < old_position:
                    zero_crossings += 1
        
    return zero_crossings, position

zero_count, final_position = get_password(rotations)
print("Times landed on 0:", zero_count)
print("Final position:", final_position)

crossing_count, _ = get_password_p2(rotations)

print(zero_count + crossing_count)