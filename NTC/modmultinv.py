# Python3 program to find modular
# inverse of A under modulo M

# A naive method to find modulor
# multiplicative inverse of A
# under modulo M


def modInverse(A, M):
	for X in range(1, M):
		if (((A % M) * (X % M)) % M == 1):
			return X
	return -1

if __name__ == "__main__":
	A = 3
	M = 11

	# Function call
	print(modInverse(A, M))


