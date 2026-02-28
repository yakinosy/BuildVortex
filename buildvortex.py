# buildvortex.py
"""
Main module for BuildVortex application.
"""

import argparse
import logging
import sys
from typing import Optional

class BuildVortex:
    """Main class for BuildVortex functionality."""
    
    def __init__(self, verbose: bool = False):
        """Initialize with verbosity setting."""
        self.verbose = verbose
        self.logger = self._setup_logging()
        
    def _setup_logging(self) -> logging.Logger:
        """Configure logging based on verbosity."""
        logger = logging.getLogger(__name__)
        level = logging.DEBUG if self.verbose else logging.INFO
        logger.setLevel(level)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        ))
        logger.addHandler(handler)
        return logger
        
    def run(self) -> bool:
        """Main execution method."""
        try:
            self.logger.info("Starting BuildVortex processing")
            # Add your main logic here
            self.logger.info("Processing completed successfully")
            return True
        except Exception as e:
            self.logger.error("Processing failed: %s", str(e), exc_info=self.verbose)
            return False

def main():
    """Command line entry point."""
    parser = argparse.ArgumentParser(description="BuildVortex - A powerful utility")
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose logging')
    args = parser.parse_args()
    
    app = BuildVortex(verbose=args.verbose)
    if not app.run():
        sys.exit(1)

if __name__ == "__main__":
    main()
