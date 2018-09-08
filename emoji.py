import random
def get_positive_emoji():
	db = [
		'hugging_face', 'thinking_face', 'man-gesturing-ok', 'woman-gesturing-ok',
		'sunglasses', 'innocent', 'pile_of_poo', 'face_with_monocle', '+1', 
		'money_mouth_face', 'ghost', 'fearful', 'baby', 'rolling_on_the_floor_laughing',
		'eyes', 'kissing_heart', 'kissing_smiling_eyes', 'blush', 'face_vomiting',
		'face_with_symbols_on_mouth'
	]
	return random.choice(db)
