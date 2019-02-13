import argparse
from embedding_visualization import visualize_embeddings
from train_featurizer import generate_dataset
from VAEFeaturizer import VAEFeaturizer
from TDCFeaturizer import TDCFeaturizer
from ForwardModelFeaturizer import ForwardModelFeaturizer


def visualize_features(videos_path, featurizer_type, initial_width, initial_height, desired_width, desired_height,costar):
	if featurizer_type == 'vae':
		featurizer_class = VAEFeaturizer
	elif featurizer_type == 'tdc':
		featurizer_class = TDCFeaturizer
	elif featurizer_type == 'forward_model':
		featurizer_class = ForwardModelFeaturizer
	else:
		raise TypeError
	    
	featurizer = featurizer_class(initial_width, initial_height, desired_width, desired_height, costar,feature_vector_size=1024, learning_rate=0.0001, experiment_name='default')


	d = generate_dataset(videos_path, 10, initial_width, initial_height, costar)
	features1 = featurizer.featurize(d[0])
	features2 = featurizer.featurize(d[1])
	#features3 = featurizer.featurize(d[2])

	features_all = [features1, features2]#, features3]
	visualize_embeddings(features_all)

if __name__ == '__main__':
	args_parser = argparse.ArgumentParser()
	args_parser.add_argument('--videos_path', help='Path for training data')
	args_parser.add_argument('--featurizer_type', help='Choose from [tdc, vae, forward_model]', default='tdc')
	args_parser.add_argument('--initial_width', help='Initial width for the videos', type=int, default=140)
	args_parser.add_argument('--initial_height', help='Initial height for the videos', type=int, default=140)
	args_parser.add_argument('--desired_width', help='Width for the videos after cropping', type=int, default=128)
	args_parser.add_argument('--desired_height', help='Height for the videos after cropping', type=int, default=128)
	args_parser.add_argument('--costar', help = 'visualize costar data', type=int,default=1)
	args = args_parser.parse_args()
	visualize_features(
		args.videos_path,
	    args.featurizer_type, 
	    args.initial_width,
	    args.initial_height,
	    args.desired_width,
	    args.desired_height,
	    args.costar
	)
	




    #visualize_features(initial_width = 92, initial_height = 92, desired_width = 84, desired_height = 84, featurizer_type = 'tdc')
