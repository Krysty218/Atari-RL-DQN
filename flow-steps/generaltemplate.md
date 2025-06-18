# Pseudo code
Initialize environment
Reset environment to get initial state

While not done:
    Choose action randomly
    Execute action in environment
    Get new observation, reward, and done signal
    Repeat

Close environment


# Python Code
import gym

env = gym.make("ENV-NAME-HERE", render_mode="human")
obs, info = env.reset()
done = False

while not done:
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)
    done = terminated or truncated
env.close()



Pseudocode	                                         Python Code
Initialize environment	                               env = gym.make("ALE/Pong-v5", render_mode="human")
Reset environment to get initial state	               obs, info = env.reset()
While not done:	                                       while not done:
→ Choose action randomly	                            action = env.action_space.sample()
→ Execute action in environment	                        obs, reward, terminated, truncated, info = env.step(action)
→ Get new observation, reward, and done signal	        Same line: all 5 values returned from env.step()
→ Repeat	Loop continues until                        done = terminated or truncated
Close environment	                                   env.close()

