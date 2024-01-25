extends Area2D
class_name DamageBody

@export var kb_vector: Vector2
@export var on_hit_damage: int


func _on_body_entered(body):
	if "hit" in body:
		body.hit(kb_vector, on_hit_damage)
