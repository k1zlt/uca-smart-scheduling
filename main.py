import yaml
import os


if __name__ == '__main__':
    with open('configuration.yaml', 'r') as conf:
        config = yaml.safe_load(conf)
    base_dir = os.path.abspath('.')
    config['dirs'] = {key: os.path.join(base_dir, value) for key, value in config['dirs'].items()}
    config['dirs']['base_dir'] = base_dir
    if config['services']['load']:
        print('Loading data from {}.'.format(config['services']['base_url']))
