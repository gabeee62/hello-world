extends CharacterBody2D

signal is_dead()

var direction: float = 0.0

@export var move_speed: float
@export var jump_height: float
@export var jump_time_to_peak: float
@export var jump_time_to_descent: float

@onready var jump_velocity: float = ((2.0 * jump_height) / jump_time_to_peak) * -1.0
@onready var jump_gravity: float = ((-2.0 * jump_height) / (jump_time_to_peak * jump_time_to_peak)) * -1.0
@onready var fall_gravity: float = ((-2.0 * jump_height) / (jump_time_to_descent * jump_time_to_descent)) * -1.0


func _process(delta):
	if Input.is_action_pressed("left"):
		direction = -1.0
	if Input.is_action_pressed("right"):
		direction = 1.0
	if not Input.is_action_pressed("left") and not Input.is_action_pressed("right"):
		direction = 0.0
	if Input.is_action_pressed("up") and is_on_floor():
		jump()
	
	velocity.x = direction * move_speed
	velocity.y += get_gravity() * delta
	move_and_slide()


func jump():
	velocity.y = jump_velocity


func get_gravity() -> float:
	if velocity.y < 0:
		return jump_gravity
	else:
		return fall_gravity


func _on_health_controller_dead():
	is_dead.emit()
