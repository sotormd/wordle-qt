#!/usr/bin/env python3

import random

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QComboBox, QGridLayout, QHBoxLayout,
                             QInputDialog, QLabel, QMessageBox, QPushButton,
                             QVBoxLayout, QWidget)

from modules import analyze, game, words
from modules.themes import styles, get_stylesheet, set_current_style

MAX_GUESSES = 6
WORD_LENGTH = 5

class WordleUI(QWidget):
    def __init__(self, app, current_style):
        super().__init__()
        self.app = app
        self.current_style = current_style
        self.setWindowTitle("Wordle")
        self.colors = styles[self.current_style]["colors"]
        self.init_game()
        self.init_ui()
        self.setFixedSize(700, 850)

    def init_game(self):
        self.word = random.choice(words.SMALL).lower()
        self.game = game.Wordle(self.word)
        self.analyzer = analyze.Analyzer(self.word, words.HUGE)
        self.current_row = 0
        self.current_col = 0
        self.guesses = [["" for _ in range(WORD_LENGTH)] for _ in range(MAX_GUESSES)]
        print(f"[DEBUG] {self.word.upper()}")

    def _style_key_default(self, btn: QPushButton):
        btn.setStyleSheet(
            f"border: 2px solid {self.colors['tile-border']}; "
            f"background-color: {self.colors['background']}; "
            f"color: {self.colors['foreground']}; "
            f"font-weight: 600; border-radius: 8px;"
        )

    def _style_key_colored(self, btn: QPushButton, bg_color: str):
        btn.setStyleSheet(
            f"border: 2px solid {self.colors['tile-border']}; "
            f"background-color: {bg_color}; "
            f"color: {self.colors['white']}; "
            f"font-weight: 700; border-radius: 8px;"
        )

    def init_ui(self):
        main_layout = QVBoxLayout()
        heading = QLabel("WORDLE")
        heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        heading.setStyleSheet(f"font-weight: bold; font-size: 18px;")
        main_layout.addWidget(heading)
        main_layout.setSpacing(10)
        self.grid = QGridLayout()
        self.grid.setHorizontalSpacing(15)
        self.grid.setVerticalSpacing(10)
        self.best_labels = []
        self.tiles = []
        self.bits_labels = []
        self.poss_labels = []
        self.keyboard_buttons = {}
        for row in range(MAX_GUESSES):
            best_label = QLabel("")
            best_label.setFixedWidth(69)
            best_label.setWordWrap(True)
            best_label.setAlignment(
                Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
            )
            best_label.hide()
            self.grid.addWidget(best_label, row, 0)
            self.best_labels.append(best_label)
            wordle_box = QHBoxLayout()
            row_tiles = []
            for col in range(WORD_LENGTH):
                tile = QLabel("")
                tile.setFixedSize(80, 80)
                tile.setAlignment(Qt.AlignmentFlag.AlignCenter)
                tile.setFont(QFont("", 32, QFont.Weight.Bold))
                tile.setStyleSheet(
                    f"border: 3px solid {self.colors['tile-border']}; "
                    f"background-color: {self.colors['background']}; "
                    f"color: {self.colors['foreground']};"
                )
                tile.state = None
                wordle_box.addWidget(tile)
                row_tiles.append(tile)
            self.tiles.append(row_tiles)
            wordle_box.setSpacing(8)
            self.grid.addLayout(wordle_box, row, 1)
            bits_label = QLabel("")
            bits_label.setFixedWidth(27)
            bits_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            bits_label.hide()
            self.grid.addWidget(bits_label, row, 2)
            self.bits_labels.append(bits_label)
            poss_label = QLabel("")
            poss_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            poss_label.setFixedWidth(27)
            poss_label.hide()
            self.grid.addWidget(poss_label, row, 3)
            self.poss_labels.append(poss_label)
        grid_wrapper = QHBoxLayout()
        grid_wrapper.addStretch()
        grid_wrapper.addLayout(self.grid)
        grid_wrapper.addStretch()
        main_layout.addLayout(grid_wrapper)
        main_layout.addSpacing(20)
        kb_wrapper = QVBoxLayout()
        rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
        self.kb_rows = []
        for r, row_letters in enumerate(rows):
            row_layout = QHBoxLayout()
            row_layout.setSpacing(6)
            if r == 2:
                enter_btn = QPushButton("ENTER")
                enter_btn.setFixedSize(88, 60)
                enter_btn.clicked.connect(lambda: self.handle_key("ENTER"))
                enter_btn.priority = -1
                self._style_key_default(enter_btn)
                row_layout.addWidget(enter_btn)
                self.keyboard_buttons["ENTER"] = enter_btn
            for letter in row_letters:
                btn = QPushButton(letter)
                btn.setFixedSize(54, 60)
                btn.clicked.connect(lambda _, l=letter: self.handle_key(l))
                btn.priority = -1
                self._style_key_default(btn)
                row_layout.addWidget(btn)
                self.keyboard_buttons[letter] = btn
            if r == 2:
                back_btn = QPushButton("󰁮")
                back_btn.setFixedSize(88, 60)
                back_btn.clicked.connect(lambda: self.handle_key("BACKSPACE"))
                back_btn.priority = -1
                self._style_key_default(back_btn)
                row_layout.addWidget(back_btn)
                self.keyboard_buttons["BACKSPACE"] = back_btn
            kb_wrapper.addLayout(row_layout)
            self.kb_rows.append(row_layout)
        main_layout.addLayout(kb_wrapper)
        btn_layout = QHBoxLayout()
        self.new_game_button = QPushButton("")
        self.new_game_button.setFixedSize(40, 40)
        self.new_game_button.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.new_game_button.clicked.connect(self.restart_game)
        btn_layout.addWidget(self.new_game_button)
        self.toggle_info_button = QPushButton("󰈈")
        self.toggle_info_button.setFixedSize(40, 40)
        self.toggle_info_button.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.toggle_info_button.setCheckable(True)
        self.toggle_info_button.setChecked(True)
        self.toggle_info_button.toggled.connect(self.toggle_info)
        btn_layout.addWidget(self.toggle_info_button)
        self.autoplay_button = QPushButton("󰚩")
        self.autoplay_button.setFixedSize(40, 40)
        self.autoplay_button.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.autoplay_button.clicked.connect(self.autoplay_game)
        btn_layout.addWidget(self.autoplay_button)
        self.custom_word_button = QPushButton("󱚌")
        self.custom_word_button.setFixedSize(40, 40)
        self.custom_word_button.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.custom_word_button.clicked.connect(self.play_custom_word)
        btn_layout.addWidget(self.custom_word_button)
        self.style_combo = QComboBox()
        self.style_combo.addItems(sorted(styles.keys()))
        self.style_combo.setFixedWidth(200)
        self.style_combo.setCurrentText(self.current_style)
        self.style_combo.currentTextChanged.connect(self.change_style)
        self.style_combo.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        btn_layout.addStretch()
        btn_layout.addWidget(self.style_combo)
        main_layout.addLayout(btn_layout)
        self.setLayout(main_layout)
        best = self.analyzer.get_best_guesses([])
        self.best_labels[0].setText("\n".join(best[:3]))

    def handle_key(self, key):
        if self.current_row >= MAX_GUESSES:
            return
        if key == "ENTER":
            if self.current_col == WORD_LENGTH:
                self.submit_guess()
        elif key == "BACKSPACE":
            if self.current_col > 0:
                self.current_col -= 1
                self.tiles[self.current_row][self.current_col].setText("")
                self.guesses[self.current_row][self.current_col] = ""
        else:
            if self.current_col < WORD_LENGTH and key.isalpha() and len(key) == 1:
                self.tiles[self.current_row][self.current_col].setText(key.upper())
                self.guesses[self.current_row][self.current_col] = key.lower()
                self.current_col += 1

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key.Key_Escape:
            self.restart_game()
            return
        if self.current_row >= MAX_GUESSES:
            return
        if Qt.Key.Key_A <= key <= Qt.Key.Key_Z:
            self.handle_key(event.text().upper())
        elif key == Qt.Key.Key_Backspace:
            self.handle_key("BACKSPACE")
        elif key in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            self.handle_key("ENTER")

    def submit_guess(self):
        guess = "".join(self.guesses[self.current_row]).lower()
        if guess not in words.HUGE:
            return
        result = self.game.guess(guess)
        color_map = {
            0: self.colors["gray"],
            1: self.colors["yellow"],
            2: self.colors["green"],
        }
        for i, score in enumerate(result):
            self.color_tile(
                self.tiles[self.current_row][i], color_map[score], state=score
            )
            self.update_keyboard(guess[i].upper(), score)
        bits, old_len, new_len = self.analyzer.analyze_guesses(
            ["".join(g).lower() for g in self.guesses[: self.current_row + 1] if any(g)]
        )[-1]
        self.bits_labels[self.current_row].setText(f"{bits:.2f}")
        self.poss_labels[self.current_row].setText(str(new_len))
        past = [
            "".join(g).lower() for g in self.guesses[: self.current_row + 1] if any(g)
        ]
        best = self.analyzer.get_best_guesses(past[:-1])
        self.best_labels[self.current_row].setText("\n".join(best[:3]))
        if guess == self.word or self.current_row + 1 == MAX_GUESSES:
            self.current_row = MAX_GUESSES
            if guess != self.word:
                msg = QMessageBox(self)
                msg.setWindowTitle("Game Over")
                msg.setText(f"The correct word was:\n\n{self.word.upper()}")
                msg.setIcon(QMessageBox.Icon.Information)
                msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg.setDefaultButton(QMessageBox.StandardButton.Ok)
                msg.setMinimumSize(300, 150)
                font = msg.font()
                font.setPointSize(12)
                font.setBold(True)
                msg.setFont(font)
                msg.exec()
        else:
            self.current_row += 1
            self.current_col = 0

    def restart_game(self):
        self.init_game()
        for row_tiles in self.tiles:
            for tile in row_tiles:
                tile.setText("")
                tile.state = None
                tile.setStyleSheet(
                    f"border: 2px solid {self.colors['tile-border']}; "
                    f"background-color: {self.colors['background']}; "
                    f"color: {self.colors['foreground']};"
                )
        for label in self.best_labels + self.bits_labels + self.poss_labels:
            label.setText("")
        for key, btn in self.keyboard_buttons.items():
            btn.priority = -1
            self._style_key_default(btn)
        best = self.analyzer.get_best_guesses([])
        self.best_labels[0].setText("\n".join(best[:3]))

    def color_tile(self, tile, bg_color, state=None):
        tile.state = state
        tile.setStyleSheet(
            f"border: 2px solid {self.colors['tile-border']}; "
            f"background-color: {bg_color}; "
            f"color: {self.colors['white']};"
        )

    def update_keyboard(self, letter: str, score: int):
        btn = self.keyboard_buttons.get(letter)
        if not btn:
            return
        new_priority = score
        if getattr(btn, "priority", -1) >= new_priority:
            return
        btn.priority = new_priority
        color_map = {
            0: self.colors["gray"],
            1: self.colors["yellow"],
            2: self.colors["green"],
        }
        self._style_key_colored(btn, color_map[new_priority])

    def toggle_info(self, checked):
        for lbl in self.best_labels + self.bits_labels + self.poss_labels:
            lbl.setVisible(not checked if False else not checked)
        if checked:
            self.toggle_info_button.setText("󰈈")
        else:
            self.toggle_info_button.setText("󰈉")

    def autoplay_game(self):
        while self.current_row < MAX_GUESSES:
            past = [
                "".join(g).lower() for g in self.guesses[: self.current_row] if any(g)
            ]
            best_guesses = self.analyzer.get_best_guesses(past)
            if not best_guesses:
                break
            guess = best_guesses[0]
            for col, letter in enumerate(guess):
                self.tiles[self.current_row][col].setText(letter.upper())
                self.guesses[self.current_row][col] = letter
            self.current_col = WORD_LENGTH
            self.submit_guess()

    def play_custom_word(self):
        text, ok = QInputDialog.getText(self, "Custom Word", "Enter a 5-letter word:")
        if not ok:
            return
        custom_word = text.strip().lower()
        print("-" + custom_word + "-")
        if len(custom_word) != 5 or not custom_word.isalpha():
            msg = QMessageBox(self)
            msg.setWindowTitle("Invalid Word")
            msg.setText("Please enter a valid 5-letter word.")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.exec()
            return
        if custom_word not in words.HUGE:
            custom_library = words.HUGE + [custom_word]
        else:
            custom_library = words.HUGE
        self.word = custom_word
        self.game = game.Wordle(self.word)
        self.analyzer = analyze.Analyzer(self.word, custom_library)
        self.current_row = 0
        self.current_col = 0
        self.guesses = [["" for _ in range(WORD_LENGTH)] for _ in range(MAX_GUESSES)]
        for row_tiles in self.tiles:
            for tile in row_tiles:
                tile.setText("")
                tile.state = None
                tile.setStyleSheet(
                    f"border: 2px solid {self.colors['tile-border']}; "
                    f"background-color: {self.colors['background']}; "
                    f"color: {self.colors['foreground']};"
                )
        for label in self.best_labels + self.bits_labels + self.poss_labels:
            label.setText("")
        for key, btn in self.keyboard_buttons.items():
            btn.priority = -1
            self._style_key_default(btn)
        best = self.analyzer.get_best_guesses([])
        self.best_labels[0].setText("\n".join(best[:3]))
        print(f"[DEBUG] Custom word set: {self.word.upper()}")

    def change_style(self, style_name):
        self.current_style = style_name
        self.colors = styles[self.current_style]["colors"]
        self.app.setStyleSheet(get_stylesheet(self.current_style))
        set_current_style(self.current_style)
        for row_tiles in self.tiles:
            for tile in row_tiles:
                if tile.state is None:
                    tile.setStyleSheet(
                        f"border: 2px solid {self.colors['tile-border']}; "
                        f"background-color: {self.colors['background']}; "
                        f"color: {self.colors['foreground']};"
                    )
                else:
                    color_map = {
                        0: self.colors["gray"],
                        1: self.colors["yellow"],
                        2: self.colors["green"],
                    }
                    self.color_tile(tile, color_map[tile.state], state=tile.state)
        for key, btn in self.keyboard_buttons.items():
            pr = getattr(btn, "priority", -1)
            if pr < 0:
                self._style_key_default(btn)
            else:
                color_map = {
                    0: self.colors["gray"],
                    1: self.colors["yellow"],
                    2: self.colors["green"],
                }
                self._style_key_colored(btn, color_map[pr])

