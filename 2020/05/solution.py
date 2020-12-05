#!/usr/bin/python3
"""
--- Day 5: Binary Boarding ---
You board your plane only to discover a new problem: you dropped your boarding
pass! You aren't sure which seat is yours, and all of the flight attendants are
busy with the flood of people that suddenly made it through passport control.

You write a quick program to use your phone's camera to scan all of the nearby
boarding passes (your puzzle input); perhaps you can find your seat through
process of elimination.

Instead of zones or groups, this airline uses binary space partitioning to seat
people. A seat might be specified like FBFBBFFRLR, where F means "front", B
means "back", L means "left", and R means "right".

The first 7 characters will either be F or B; these specify exactly one of the
128 rows on the plane (numbered 0 through 127). Each letter tells you which
half of a region the given seat is in. Start with the whole list of rows; the
first letter indicates whether the seat is in the front (0 through 63) or the
back (64 through 127). The next letter indicates which half of that region the
seat is in, and so on until you're left with exactly one row.

For example, consider just the first seven characters of FBFBBFFRLR:

Start by considering the whole range, rows 0 through 127.
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.
The final F keeps the lower of the two, row 44.
The last three characters will be either L or R; these specify exactly one of
the 8 columns of seats on the plane (numbered 0 through 7). The same process as
above proceeds again, this time with only three steps. L means to keep the
lower half, while R means to keep the upper half.

For example, consider just the last 3 characters of FBFBBFFRLR:

Start by considering the whole range, columns 0 through 7.
R means to take the upper half, keeping columns 4 through 7.
L means to take the lower half, keeping columns 4 through 5.
The final R keeps the upper of the two, column 5.
So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the
column. In this example, the seat has ID 44 * 8 + 5 = 357.

Here are some other boarding passes:

BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.
As a sanity check, look through your list of boarding passes. What is the
highest seat ID on a boarding pass?

--- Part Two ---
Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

It's a completely full flight, so your seat should be the only missing boarding
pass in your list. However, there's a catch: some of the seats at the very
front and back of the plane don't exist on this aircraft, so they'll be missing
from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and
-1 from yours will be in your list.

What is the ID of your seat?
"""


def readInput():
    with open('./input.txt', 'r') as f:
        boarding_passes = [i.strip() for i in f.readlines()]
        return boarding_passes


def findRow(row_code, row_list):
    row = 0
    new_row_list = []
    if len(row_code) == 1:
        if row_code == "F":
            row = row_list[0]
        else:
            row = row_list[1]
    else:
        mid = int(len(row_list) / 2)
        if row_code[0] == "F":
            new_row_list = row_list[:mid]
        else:
            new_row_list = row_list[mid:]
        row = findRow(row_code[1:], new_row_list)
    return row


def findSeat(seat_code, seat_list):
    seat = 0
    new_seat_list = []
    if len(seat_code) == 1:
        if seat_code == "L":
            seat = seat_list[0]
        else:
            seat = seat_list[1]
    else:
        mid = int(len(seat_list) / 2)
        if seat_code[0] == "L":
            new_seat_list = seat_list[:mid]
        else:
            new_seat_list = seat_list[mid:]
        seat = findSeat(seat_code[1:], new_seat_list)
    return seat


def part1(boarding_passes):
    max_id = 0
    for boarding_pass in boarding_passes:
        row_code = boarding_pass[:-3]
        seat_code = boarding_pass[7:]
        row = findRow(row_code, list(range(128)))
        seat = findSeat(seat_code, list(range(8)))
        curr_id = (row * 8) + seat
        if curr_id > max_id:
            max_id = curr_id

    print("Part 1: Max ID: {}".format(max_id))


def part2(boarding_passes):
    my_seat_id = 0
    boarding_ids = []
    for boarding_pass in boarding_passes:
        row_code = boarding_pass[:-3]
        seat_code = boarding_pass[7:]
        row = findRow(row_code, list(range(128)))
        seat = findSeat(seat_code, list(range(8)))
        curr_id = (row * 8) + seat
        boarding_ids.append(curr_id)
    boarding_ids.sort()
    for i in range(len(boarding_ids) - 1):
        diff = boarding_ids[i + 1] - boarding_ids[i]
        if diff == 2:
            my_seat_id = boarding_ids[i] + 1
            break
    print("Part 2: My seat ID: {}".format(my_seat_id))


def main():
    boarding_passes = readInput()
    part1(boarding_passes)
    part2(boarding_passes)


if __name__ == '__main__':
    main()
