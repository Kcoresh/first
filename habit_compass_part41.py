# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: HabitCompass
def dry_run(operation, data, context=None):
    """Execute operation in read-only / simulated mode, returning the result without mutating state."""
    import copy as _copy
    
    def safe_get(obj, key, default=None):
        if isinstance(obj, dict) and key in obj:
            return obj[key]
        elif hasattr(obj, 'get'):
            try:
                return obj.get(key, default)
            except (AttributeError, TypeError):
                pass
        return default
    
    def deep_copy(obj):
        """Create a shallow copy for simple types and dict-like objects."""
        if isinstance(obj, (str, int, float, bool)):
            return obj
        elif isinstance(obj, dict):
            return {k: deep_copy(v) for k, v in obj.items()}
        else:
            return _copy.copy(obj)

    def build_output(operation_name, input_data, context=None):
        """Construct a dry-run output with operation name, original data, and simulated result."""
        base = {"operation": operation_name, "status": "dry_run", "input": deep_copy(input_data)}
        if context:
            base["context"] = deep_copy(context)
        
        # Simulate result based on operation type
        if operation_name in ("add_habit", "update_series", "create_note"):
            if isinstance(operation, dict):
                base["simulated_result"] = {"success": True, "message": f"{operation_name} simulated successfully"}
                base["original_data"] = deep_copy(input_data)
        elif operation_name in ("delete_habit", "clear_series"):
            if isinstance(operation, dict):
                base["simulated_result"] = {"success": False, "reason": "dry_run prevents deletion"}
        else:
            base["simulated_result"] = {"success": None, "message": f"No simulation for {operation_name}"}

        return base
    
    return build_output(operation if isinstance(operation, str) else operation.get("operation", operation), data if not isinstance(data, dict) or 'operation' in data else data, context)
