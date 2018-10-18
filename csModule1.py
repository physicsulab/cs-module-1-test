import numpy as np
import math as m

# Helpers
def error_output_unhelpful(cp_num):
	"""
	Prints error message (unhelpful).
	"""
	return "Checkpoint {0} Failed!\nTry again.".format(cp_num)


def error_output_helpful(cp_num, expected, actual):
	"""
	Prints error message with expected value.
	"""
	return "Checkpoint {0} Failed!\nExpected: {1}\nGot: {2}".format(cp_num, expected, actual)


def success(cp_num):
	"""
	Prints success message.
	"""
	print("Checkpoint {0} passed!".format(cp_num))


# Tests
def checkpoint1(cp1):
	"""
	Remainder of {e to the power 15 times 45} divided by 6?
	"""
	expected = (m.e ** 15) * 45 % 6
	assert expected == cp1, error_output_helpful(1, expected, cp1)
	success(1)


def checkpoint2(cp2):
	"""
	Guess the value in x.
	"""
	x = 5 * 2 + 1
	x = x + 1
	y = 2 * x
	x = x + y
	expected = x
	assert expected == cp2, error_output_unhelpful(2)
	success(2)


def checkpoint3(cp3):
	"""
	Which of the following are valid names?

	 ["2_cool_4_skool", "AToZ", "_model_feet", "triangle_lengths", "cats 15", "cats15"]

	"""
	expected = ["AToZ", "_model_feet", "triangle_lengths", "cats15"]
	assert type(cp3) == list, "Checkpoint 3 Failed!\nPlease enter input in a list."
	assert set(expected) == set(cp3), error_output_unhelpful(3)
	success(3)


def checkpoint4(cp4):
	"""
	Types of each of the following?

	 [[], 45, 8932.32, "hi, nice to meet you", -88, 0, (55, 55), {"0": "wish", "14": "circles"}, False]

	"""
	expected = [list, int, float, str, int, int, tuple, dict, bool]
	assert type(cp4) == list, "Checkpoint 4 Failed!\nPlease enter input in order in a list."
	assert expected == cp4, error_output_unhelpful(4)
	success(4)


def checkpoint5(cp5):
	"""
	Reverse this list

	 ["alligator", "bathtub", "cat", "dog", "eggs", "spam", "basket"]

	"""
	expected = ["basket", "spam", "eggs", "dog", "cat", "bathtub", "alligator"]
	assert expected == cp5, error_output_unhelpful(5)
	success(5)


def checkpoint6(cp6):
	"""
	Original:

	 {"star": 0, "asteroids": "many", "star_type": "main-sequence", "age": "4.6 billion years"}

	Insert keys: ("planets", 8), ("dwarf_planets", 1)
	Modify key: ("star", 0) -> ("star", 1)
	"""
	expected = {"star": 1, "asteroids": "many", "star_type": "main-sequence", "age": "4.6 billion years", "dwarf_planets": 1, "planets": 8}
	assert expected == cp6, error_output_unhelpful(6)
	success(6)


# def checkpoint7(cp7):
# Nothing to check

def checkpoint8(cp8):
	"""
	Make a function:
	1) if the person is older than 65 years, return "You are a senior!" 
	2) if the person is younger than 18 years, 
		return "You are a child. You will be 18 in a few years!" 
	3) if the person is between these ages, return "You're an adult."
	"""
	assert "You are a senior!" == cp8(70), error_output_unhelpful(8)
	assert "You are a senior!" == cp8(110), error_output_unhelpful(8)
	assert "You're an adult." == cp8(65), error_output_unhelpful(8)
	assert "You're an adult." == cp8(62), error_output_unhelpful(8)
	assert "You're an adult." == cp8(25), error_output_unhelpful(8)
	assert "You're an adult." == cp8(55), error_output_unhelpful(8)
	assert "You're an adult." == cp8(18), error_output_unhelpful(8)
	assert "You are a child. You will be 18 in a few years!" == cp8(5), error_output_unhelpful(8)
	assert "You are a child. You will be 18 in a few years!" == cp8(0), error_output_unhelpful(8)
	success(8)

def checkpoint9(cp9):
	"""
	Define a function that decides if a number is prime.
	"""
	assert True == cp9(37), error_output_unhelpful(9)
	assert True == cp9(53), error_output_unhelpful(9)
	assert False == cp9(26), error_output_unhelpful(9)
	assert True == cp9(103), error_output_unhelpful(9)
	assert False == cp9(1024), error_output_unhelpful(9)
	assert True == cp9(97), error_output_unhelpful(9)
	success(9)

# def checkpoint10(cp10):
# Nothing to check

# def checkpoint9(cp11):
# Nothing to check

# def checkpoint9(cp12):
# Nothing to check

def all_checkpoints(cp1, cp2, cp3, cp4, cp5, cp6, cp8, cp9):
	checkpoint1(cp1)
	checkpoint2(cp2)
	checkpoint3(cp3)
	checkpoint4(cp4)
	checkpoint5(cp5)
	checkpoint6(cp6)
	checkpoint8(cp8)
	checkpoint9(cp9)