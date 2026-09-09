# compiler and flags
CC = gcc
CFLAGS = -Wall -Wextra -std=c11

# list of object files for Lab 2
OBJECTS = main.o isOdd.o isEven.o

# final exe file name
TARGET = isEvenOdd

all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# remove .o files
clean:
	rm -rf *.o $(TARGET)
