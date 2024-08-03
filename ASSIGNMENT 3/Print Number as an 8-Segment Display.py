def print_segment_display(n):
    segments = {
        0: [" _ ", "| |", "|_|"],
        1: ["   ", "  |", "  |"],
        2: [" _ ", " _|", "|_ "],
        3: [" _ ", " _|", " _|"],
        4: ["   ", "|_|", "  |"],
        5: [" _ ", "|_ ", " _|"],
        6: [" _ ", "|_ ", "|_|"],
        7: [" _ ", "  |", "  |"],
        8: [" _ ", "|_|", "|_|"],
        9: [" _ ", "|_|", " _|"]
    }
    
    for i in range(3):
        for digit in str(n):
            print(segments[int(digit)][i], end=" ")
        print()
n = int(input("Enter a number: "))
print_segment_display(n)