# rl_agent/utils/reward_shaping.py

def custom_reward(state, action, done, info):
    reward = 0

    if info.get("phishing_detected"):
        reward += 10  # Reward for detecting phishing
    if info.get("false_positive"):
        reward -= 5   # Penalty for false positive
    if done and not info.get("phishing_detected"):
        reward -= 10  # Penalty for missing threat

    return reward

