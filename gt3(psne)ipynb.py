# -*- coding: utf-8 -*-
"""GT3(PSNE)ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UMswlHYgrRcrpbdx_AASOKX2iPyj6B0T
"""

import random
def coin_duel():
  choices = ["Attack", "Defend"]
 # Simultaneous choice by both players
  player1_choice = random.choice(choices)
  player2_choice = random.choice(choices)
 # Resolve the choices and determine points
  if player1_choice == "Attack" and player2_choice == "Attack":
    return -1, -1
  elif player1_choice == "Defend" and player2_choice == "Defend":
    return 1, 1
  elif player1_choice == "Attack" and player2_choice == "Defend":
    return 2, -1
  else:
    return -1, 2
# Play multiple rounds to observe the lack of PSNE
for _ in range(5):
  result = coin_duel()
  print(f"Player 1 score: {result[0]}, Player 2 score: {result[1]}")