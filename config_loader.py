"""Configuration loader for numerical methods project."""
import json
import os
from typing import Any, Optional


class ConfigLoader:
    """Loads and manages configuration from config.json."""
    
    def __init__(self, config_path: str = "config.json"):
        """Initialize the config loader.
        
        Args:
            config_path: Path to the configuration file
        """
        self.config_path = config_path
        self._config = self.load_config()
    
    def load_config(self) -> dict:
        """Load configuration from JSON file.
        
        Returns:
            Dictionary containing configuration data
        """
        try:
            if os.path.exists(self.config_path):
                with open(self.config_path, 'r') as f:
                    return json.load(f)
            else:
                # Return default configuration
                return {
                    "max_iterations": 100,
                    "tolerance": 1e-6,
                    "jacobi": {
                        "max_iterations": 100,
                        "tolerance": 1e-6,
                        "relaxation_factor": 1.0
                    },
                    "regula_falsi": {
                        "max_iterations": 100,
                        "tolerance": 1e-6
                    },
                    "finite_difference": {
                        "default_h": 0.01,
                        "min_h": 1e-10,
                        "max_h": 1.0
                    }
                }
        except Exception as e:
            print(f"Error loading config: {e}")
            return {}
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value by key.
        
        Args:
            key: Configuration key (supports dot notation, e.g., 'jacobi.tolerance')
            default: Default value if key not found
            
        Returns:
            Configuration value or default
        """
        keys = key.split('.')
        value = self._config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def reload(self):
        """Reload configuration from file."""
        self._config = self.load_config()


# Global configuration instance
config = ConfigLoader()
