"""Kinetic Anomaly Detection Engine System (KADES)

Chain Analysis Module

This module provides core functionality for blockchain data analysis,
including transaction monitoring, pattern detection, and liquidity tracking.

Author: KADES Team
License: Proprietary"""

from .blockchain_listener import BlockchainListener
from .transaction_analyzer import TransactionAnalyzer
from .liquidity_tracker import LiquidityTracker
from .wallet_profiler import WalletProfiler

__version__ = '1.0.0'
__author__ = 'KADES Team'
__email__ = 'contact@kades.ai'

# Export main classes for easier access
__all__ = [
    'BlockchainListener',
    'TransactionAnalyzer',
    'LiquidityTracker',
    'WalletProfiler',
]

# Default configuration
DEFAULT_CONFIG = {
    'rpc_endpoint': 'https://api.mainnet-beta.solana.com',
    'update_interval': 60,  # seconds
    'max_batch_size': 100,
    'cache_duration': 3600,  # 1 hour
}
