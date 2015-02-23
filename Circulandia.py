
class SegmentoRecto:
	pass


class RectaCirculo(SegmentoRecto):
	pass


class Circulito(RectaCirculo):
	pass


class FiguraSocial(SegmentoRecto):
	pass


class Formador(FiguraSocial):
	pass


class FiguraRegular(FiguraSocial, RectaCirculo):
	pass

