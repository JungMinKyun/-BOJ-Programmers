{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ABDCEFG\n",
      "DBAECFG\n",
      "DBEGFCA"
     ]
    }
   ],
   "source": [
    "# 백준 1991번 \n",
    "\n",
    "import sys\n",
    "input = sys.stdin.readline\n",
    "\n",
    "class Node:\n",
    "    def __init__(self, key):\n",
    "        self.key = key\n",
    "        self.left = None\n",
    "        self.right = None\n",
    "\n",
    "    def __str__(self):\n",
    "        return self.key\n",
    "    \n",
    "    def set_left(self, left):\n",
    "        self.left = left\n",
    "\n",
    "    def set_right(self, right):\n",
    "        self.right = right\n",
    "\n",
    "n = int(input())\n",
    "nodes = [Node(chr(i+65)) for i in range(n)]\n",
    "\n",
    "for _ in range(n):\n",
    "    key, left, right = input().strip().split()\n",
    "    key = ord(key) - 65\n",
    "\n",
    "    if left != '.':\n",
    "        nodes[key].set_left(nodes[ord(left)-65])\n",
    "    if right != '.':\n",
    "        nodes[key].set_right(nodes[ord(right)-65])\n",
    "\n",
    "def preorder(node):\n",
    "    print(node.key, end='')\n",
    "    if node.left:\n",
    "        preorder(node.left)\n",
    "    if node.right:\n",
    "        preorder(node.right)\n",
    "\n",
    "def inorder(node):\n",
    "    if node.left:\n",
    "        inorder(node.left)\n",
    "    print(node.key, end='')\n",
    "    if node.right:\n",
    "        inorder(node.right)\n",
    "\n",
    "def postorder(node):\n",
    "    if node.left:\n",
    "        postorder(node.left)\n",
    "    if node.right:\n",
    "        postorder(node.right)\n",
    "    print(node.key, end='')\n",
    "\n",
    "preorder(nodes[0])\n",
    "print()\n",
    "inorder(nodes[0])\n",
    "print()\n",
    "postorder(nodes[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
