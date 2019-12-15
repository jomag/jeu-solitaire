#include <stdint.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int best = -1;
struct timespec start_time;

void try_all_balls(const char *board, int rows, int cols);

uint64_t elapsed_us()
{
    struct timespec end;
    clock_gettime(CLOCK_MONOTONIC_RAW, &end);
    return (end.tv_sec - start_time.tv_sec) * 1000000 + (end.tv_nsec - start_time.tv_nsec) / 1000;
}

void print_board(const char *board, int rows, int cols)
{
    for (int i = 0; i < rows; i++)
    {
        printf("%.*s\n", 7, board + cols * i);
    }
}

char *copy_board(const char *board, int rows, int cols)
{
    char *new_board = malloc(rows * cols);
    memcpy(new_board, board, rows * cols);
    return new_board;
}

int try_all_directions(const char *board, int rows, int cols, int x, int y)
{
    int locked = 1;

    if (y >= 2 && board[(y - 1) * cols + x] == 'O' && board[(y - 2) * cols + x] == '.')
    {
        char *new_board = copy_board(board, rows, cols);
        new_board[y * cols + x] = '.';
        new_board[(y - 1) * cols + x] = '.';
        new_board[(y - 2) * cols + x] = 'O';
        locked = 0;
        try_all_balls(new_board, rows, cols);
        free(new_board);
    }

    if (y < rows - 2 && board[(y + 1) * cols + x] == 'O' && board[(y + 2) * cols + x] == '.')
    {
        char *new_board = copy_board(board, rows, cols);
        new_board[y * cols + x] = '.';
        new_board[(y + 1) * cols + x] = '.';
        new_board[(y + 2) * cols + x] = 'O';
        locked = 0;
        try_all_balls(new_board, rows, cols);
        free(new_board);
    }

    if (x >= 2 && board[y * cols + x - 1] == 'O' && board[y * cols + x - 2] == '.')
    {
        char *new_board = copy_board(board, rows, cols);
        new_board[y * cols + x] = '.';
        new_board[y * cols + x - 1] = '.';
        new_board[y * cols + x - 2] = 'O';
        locked = 0;
        try_all_balls(new_board, rows, cols);
        free(new_board);
    }

    if (x < cols - 2 && board[y * cols + x + 1] == 'O' && board[y * cols + x + 2] == '.')
    {
        char *new_board = copy_board(board, rows, cols);
        new_board[y * cols + x] = '.';
        new_board[y * cols + x + 1] = '.';
        new_board[y * cols + x + 2] = 'O';
        locked = 0;
        try_all_balls(new_board, rows, cols);
        free(new_board);
    }

    return locked;
}

void try_all_balls(const char *board, int rows, int cols)
{
    int remaining = 0;
    int all_locked = 1;

    for (int y = 0; y < rows; y++)
    {
        for (int x = 0; x < cols; x++)
        {
            if (board[y * cols + x] == 'O')
            {
                remaining++;
                int locked = try_all_directions(board, rows, cols, x, y);
                if (!locked)
                {
                    all_locked = 0;
                }
            }
        }
    }

    if (all_locked)
    {
        if (best < 0 || remaining < best)
        {
            best = remaining;
            printf("%d remaining after %llu ms\n", remaining, elapsed_us() / 1000L);
            print_board(board, rows, cols);
            printf("\n");
        }
    }
}

int main(int argc, char *argv[])
{
    const char *board =
        "  OOO  "
        " OOOOO "
        "OO...OO"
        "OO...OO"
        "OO...OO"
        " OOOOO "
        "  OOO  ";
    const int rows = 7;
    const int cols = 7;

    clock_gettime(CLOCK_MONOTONIC_RAW, &start_time);

    print_board(board, rows, cols);
    try_all_balls(board, rows, cols);
    return 0;
}
