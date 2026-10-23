import typing
import time


class Text:
	@staticmethod
	def typewriter_effect(
		text: str,
		delay: float
	) -> None:

		for letter in text:
			time.sleep(delay)
			print(letter, end="", flush=True)

	@staticmethod
	def dialog(
		speaker1: list[str],
		speaker2: list[str],
		use_typewriter_effect: bool=False,
		typewriter_speed: float=0
	) -> None:

		# 
		pass

	@staticmethod
	def mutiple_choices(
		self,
		question: str,
		expression: bool,
		multiple_questions: list[str]
	) -> None:

		# Print the question
		# Use a match case on the expression
		# Ask the multiple questions
		# Return the response
		pass
	
	def get_player_int_input(
		ask_message: str,
		ask_again_message: str,
		desired_awnser_range: tuple[str | int]
	) -> int:

		response: str = input(ask_message).strip()\
										  .lower()

		if response.isnumeric()\
		and int(response) in desired_awnser_range:
			return int(response)

		while response not in desired_awnser_range:
			try:
				response = int(
					input(ask_again_message).strip()\
											.lower()
				)
			except ValueError:
				print("Não use letra ou símbolos.")

		return response


if __name__ == "__main__":

	print(
		Text.get_player_int_input(
			"Escolha um número entre [ 1 / 2 / 3 ]: ",
			"Resposta inválida: Escolha um número entre [ 1 / 2 / 3 ]: ",
			(1, 2, 3)
		)
	)

	phrase: str = "Apenas testando para ver se dá certo, espero que sim, né?"
	Text.typewriter_effect(
		phrase,
		0.08
	)

	print(f"\r{len(phrase)*" "}")
	print("\rolá")
