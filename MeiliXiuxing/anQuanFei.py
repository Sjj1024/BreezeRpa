import secretflow as sf

# In case you have a running secretflow runtime already.
sf.shutdown()

sf.init(['alice', 'bob', 'carol'], address='local')
alice, bob, carol = sf.PYU('alice'), sf.PYU('bob'), sf.PYU('carol')

import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
data = pd.concat([iris.data, iris.target], axis=1)

# Horizontal partitioning.
h_alice, h_bob, h_carol = data.iloc[:40, :], data.iloc[40:100, :], data.iloc[100:, :]

# Save to temporary files.
import tempfile
import os

temp_dir = tempfile.mkdtemp()

h_alice_path = os.path.join(temp_dir, 'h_alice.csv')
h_bob_path = os.path.join(temp_dir, 'h_bob.csv')
h_carol_path = os.path.join(temp_dir, 'h_carol.csv')
h_alice.to_csv(h_alice_path, index=False)
h_bob.to_csv(h_bob_path, index=False)
h_carol.to_csv(h_carol_path, index=False)


h_alice.head(), h_bob.head(), h_carol.head()


# Vertical partitioning.
v_alice, v_bob, v_carol = data.iloc[:, :2], data.iloc[:, 2:4], data.iloc[:, 4:]

# Save to temporary files.
v_alice_path = os.path.join(temp_dir, 'v_alice.csv')
v_bob_path = os.path.join(temp_dir, 'v_bob.csv')
v_carol_path = os.path.join(temp_dir, 'v_carol.csv')
v_alice.to_csv(v_alice_path, index=False)
v_bob.to_csv(v_bob_path, index=False)
v_carol.to_csv(v_carol_path, index=False)


v_alice, v_bob, v_carol