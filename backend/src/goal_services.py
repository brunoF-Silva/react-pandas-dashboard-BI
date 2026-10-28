from typing import Dict, Any

class Goal:
    def __init__(self, id: int, target_value: float, operator: str, description: str):
        self.id = id
        self.target_value = target_value
        self.operator = operator
        self.description = description

    def evaluate(self, current_value: float) -> Dict[str, Any]:
        if self.operator == 'greater_than':
            is_met = current_value > self.target_value
        elif self.operator == 'less_than':
            is_met = current_value < self.target_value
        elif self.operator == 'equals':
            is_met = current_value == self.target_value
        else:
            is_met = False

        return {
            'id': self.id,
            'target_value': self.target_value,
            'description': self.description,
            'is_met': int(is_met)
        }