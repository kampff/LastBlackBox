# -*- coding: utf-8 -*-
"""
LBB: Material Class

@author: kampff
"""

# Import libraries
import json

# Import modules
import LBB.lesson as Lesson

# Material Class
class Material:
    def __init__(self, text=None, dictionary=None):
        self.index = None               # Box index
        self.name = None                # Box name
        self.slug = None                # Box slug (URL)
        self.description = None         # Box description
        self.lessons = None             # Box lessons
        if text:
            self.parse(text)            # Parse box from "lessons.md" text
        elif dictionary:
            self.from_dict(dictionary)  # Load box from dictionary
        return

    # Convert box object to dictionary
    def to_dict(self):
        dictionary = {
            "index": self.index,
            "name": self.name,
            "slug": self.slug,
            "description": self.description,
            "lessons": [lesson.to_dict() for lesson in self.lessons]
        }
        return dictionary

    # Convert dictionary to box object
    def from_dict(self, dictionary):
        self.index = dictionary.get("index")
        self.name = dictionary.get("name")
        self.slug = dictionary.get("slug")
        self.description = dictionary.get("description")
        self.lessons = [Lesson.Lesson(dictionary=lesson_dictionary) for lesson_dictionary in dictionary.get("lessons", [])]
        return
    
    # Parse box string
    def parse(self, text):
        # Set line counter
        line_count = 0
        max_count = len(text)

         # Extract name
        self.name = text[0][2:]
        self.slug = self.name.lower().replace(' ', '-')
        line_count += 1

        # Extract description
        self.description = text[line_count]
        line_count += 1

        # Extract lessons
        self.lessons = []
        lesson_count = 0
        while line_count < max_count:
            lesson_text = []
            lesson_text.append(text[line_count])         # Append lesson heading
            line_count += 1
            while not text[line_count].startswith('##'): # Next lesson
                lesson_text.append(text[line_count])
                line_count += 1
                if line_count >= max_count:
                    break
            lesson = Lesson.Lesson(lesson_text)
            lesson.index = lesson_count
            self.lessons.append(lesson)
            lesson_count += 1
        return

    def render(self):
        output = ''
        return output

    # Load box object from JSON
    def load(self, path):
        with open(path, "r") as file:
            self.from_dict(json.load(file))
        return

    # Store box object in JSON file
    def store(self, path):
        with open(path, "w") as file:
            json.dump(self.to_dict(), file, indent=4)
        return
#FIN