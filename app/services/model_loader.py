import joblib
import torch


class ModelLoader:
    def load_ccn_extractor():
        """
        Load the pytorch model and sent it to the m4 gpu(mps)
        """
        torch.adaptive_avg_pool1d()
        pass

    def load_classifier():
        """
        Load the .pkl file containing the trained model - (svm, knn, or nn)
        """
        joblib.load()
        pass
