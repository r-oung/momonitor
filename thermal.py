import seeed_mlx9064x
import time

frame = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    3, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    4, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    5, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    6, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    7, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    8, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    9, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    12, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
    ]


# def fancy_print(frame):
#     index = 0
#     for row in range(12):
#         line = []
#         for col in range(16):
#            line.append(frame[index])
#            index += 1
#         print(['{:.3}'.format(px) for px in line])

# def main():
#     mlx = seeed_mlx9064x.grove_mxl90641()
#     mlx.refresh_rate = seeed_mlx9064x.RefreshRate.REFRESH_32_HZ  # fastest rate for raspberry 4 
#     frame = [0] * 16 * 12 # 16 x 12 pixel IR thermal sensor array (MLX90641)
#     time.sleep(1)
    
#     while True:
#         start = time.time()
#         mlx.getFrame(frame)
#         end = time.time()
        
#         fancy_print(frame)
#         print('Frequency: {:.3} Hz'.format(1.0 / (end - start)))

if __name__  == '__main__':
    main()
