# 🎮 3D AI Agent Tic-Tac-Toe

![header](https://capsule-render.vercel.app/api?type=waving&color=F6D860&height=160&section=header&text=3D%20Tic-Tac-Toe%20AI&fontSize=38&fontColor=111111&fontAlignY=50&animation=fadeIn)

> A three-dimensional Tic-Tac-Toe game with an AI opponent that actually makes you think.

![Python](https://img.shields.io/badge/Python-F6D860?style=for-the-badge&logo=python&logoColor=111111)
![Algorithm](https://img.shields.io/badge/MiniMax-EDE8D5?style=for-the-badge&logoColor=111111)
![Pruning](https://img.shields.io/badge/Alpha--Beta%20Pruning-EDE8D5?style=for-the-badge&logoColor=111111)

---

## 🧠 How It Works

Standard Tic-Tac-Toe is solved — any decent player knows every move. This project expands the game into **3 dimensions**, creating a much larger and more complex state space.

The AI uses the **MiniMax algorithm** to search through possible future moves and pick the optimal one. **Alpha-beta pruning** cuts off branches that can't possibly improve the result, making the search efficient enough to run in real time.

**Difficulty levels** are implemented by controlling the lookahead depth — how many moves ahead the algorithm searches. Shallow depth = easier opponent. Full depth = good luck.

---

## 🕹️ How to Run

**Requirements:** Python 3

```bash
git clone https://github.com/rawdaG/Projects.git
cd Projects/3D-Tic-Tac-Toe
python3 code.py
```

---

## ✨ What I Learned

- Implementing MiniMax from scratch
- How alpha-beta pruning reduces computation without affecting results
- Managing 3D board state in Python
- Balancing difficulty via search depth tuning

---

[![Back to Projects](https://img.shields.io/badge/←%20Back%20to%20Projects-F6D860?style=for-the-badge&logoColor=111111)](../README.md)

![footer](https://capsule-render.vercel.app/api?type=waving&color=F6D860&height=100&section=footer)
