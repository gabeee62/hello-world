extends Node

signal dead()

@export var max_health: int
var current_health: int = max_health


func _process(_delta):
	if current_health <= 0:
		death()


func heal(heal_amount):
	damage(-heal_amount)


func damage(dmg):
	var _previous_health = current_health
	current_health -= dmg


func death():
	dead.emit()
