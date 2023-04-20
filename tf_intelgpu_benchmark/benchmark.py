import os
import time
import tensorflow.compat.v1 as tf
tf.enable_eager_execution(tf.ConfigProto(log_device_placement=True))

def measure_execution_time(device, matrix_size):
    with tf.device(device):
        # Création de matrices aléatoires
        matrix1 = tf.random.uniform(shape=(matrix_size, matrix_size), minval=0, maxval=1)
        matrix2 = tf.random.uniform(shape=(matrix_size, matrix_size), minval=0, maxval=1)

        # Démarrage du chronomètre
        start_time = time.time()

        # Exécution de la multiplication de matrices
        result = tf.matmul(matrix1, matrix2)

        # Arrêt du chronomètre
        elapsed_time = time.time() - start_time

    return elapsed_time

def main():
    matrix_size = 10000

    # Mesurer le temps d'exécution sur le CPU
    cpu_time = measure_execution_time('/cpu:0', matrix_size)
    print(f"Temps d'exécution sur le CPU : {cpu_time:.4f} secondes")


    # Mesurer le temps d'exécution sur le GPU avec DirectML
    gpu_time = measure_execution_time('/dml:0', matrix_size)
    print(f"Temps d'exécution sur le GPU avec DirectML : {gpu_time:.4f} secondes")
    print(f"Le GPU a été {cpu_time / gpu_time:.2f} fois plus rapide que le CPU.")


if __name__ == "__main__":
    main()
