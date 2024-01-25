extends CharacterBody2D

signal is_dead()

var in_control: bool = true
var direction: float = 0.0
var move_speed: float

@export var walk_speed: float
@export var run_speed: float
@export var jump_height: float
@export var jump_time_to_peak: float
@export var jump_time_to_descent: float

@onready var jump_velocity: float = ((2.0 * jump_height) / jump_time_to_peak) * -1.0
@onready var jump_gravity: float = ((-2.0 * jump_height) / (jump_time_to_peak * jump_time_to_peak)) * -1.0
@onready var fall_gravity: float = ((-2.0 * jump_height) / (jump_time_to_descent * jump_time_to_descent)) * -1.0


func _process(delta):
	var direction_name = ["left", "right"]
	var direction_value = [-1.0, 1.0]
	var left_or_right = false
	
	if is_on_floor():
		in_control = true
	
	if in_control:
		for i in direction_name:
			if Input.is_action_pressed(i):
				left_or_right = true
				direction = direction_value[direction_name.find(i)]
				if Input.is_action_pressed("run"):
					move_speed = run_speed
				else:
					move_speed = walk_speed
		if not left_or_right:
			direction = 0.0
		if direction > 0:
			$Sprite2D.flip_h = false
		elif direction < 0.0:
			$Sprite2D.flip_h = true
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


func hit(vector: Vector2, _damage: int):
	velocity.y = vector.y
	move_speed = vector.x
	await get_tree().create_timer(0.01).timeout
	in_control = false
	if $Sprite2D.flip_h:
		direction = 1.0
	else:
		direction = -1.0


func _on_health_controller_dead():
	is_dead.emit()
