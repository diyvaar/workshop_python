{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "24661942",
   "metadata": {},
   "outputs": [],
   "source": [
    "#BAB6 Module"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "254a7c18",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Fibonacci numbers module\n",
    "def fib(n):    # write Fibonacci series up to n\n",
    "    a, b = 0, 1\n",
    "    while a < n:\n",
    "        print(a, end=' ')\n",
    "        a, b = b, a+b\n",
    "    print()\n",
    "    \n",
    "def fib2(n):   # return Fibonacci series up to n\n",
    "    result = []\n",
    "    a, b = 0, 1\n",
    "    while a < n:\n",
    "        result.append(a)\n",
    "        a, b = b, a+b\n",
    "    return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "c83e3743",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 \n"
     ]
    }
   ],
   "source": [
    "fib(1000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "80c00242",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fib2(100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "596e5ec7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'fibo'"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fibo.__name__"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "1cd92d7e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 \n"
     ]
    }
   ],
   "source": [
    "fib(500)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
