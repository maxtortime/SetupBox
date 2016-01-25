# TODO changes static libraries to shared
CC=gcc -std=c89 -Wall
SRC=vcscontroller.c
OBJ=vcscontroller.o
LIB=-lgit2
LIB_NAME=libsetupbox.a

all: $(OBJ)
	ar -cvq $(LIB_NAME) $(OBJ)

$(OBJ): $(SRC)
	$(CC) -c $(SRC)

clean:
	rm *.o
