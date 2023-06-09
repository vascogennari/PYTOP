import os

# ------------------------- #
input_path  = '/Users/vascogennari/Documents/work/code/python/results/GW190521_074359/PROD2/TEOBPM'
output_path = '/Users/vascogennari/Documents/work/code/python/PYTOP/samples/GW190521_074359/PROD2/TEOBPM'

elements = {
    'name'     : '',
    'pipeline' : 'pyRing',
    'model'    : '',
    'submodel' : '',
    'time'     : '',
    'GR_tag'   : 'GR',
}
# ------------------------- #

print('\nCopying samples.\nFrom:\t{input_path}\nTo:\t{output_path}\n'.format(input_path = input_path, output_path = output_path))

# Create output Evidences directory
output_evidence_dir = os.path.join(output_path, 'noise_evidences')
if not os.path.exists(output_evidence_dir): os.makedirs(output_evidence_dir)

# Create output SNR directory
output_SNR_dir      = os.path.join(output_path, 'SNR_samples')
if not os.path.exists(output_SNR_dir): os.makedirs(output_SNR_dir)

# Loop on the different runs
for file in os.listdir(input_path):
    if not file == '.DS_Store':

        i = 0
        keys = []
        tmp = file.split('_')
        for element in elements:
            if elements[element] == '':
                keys.append(tmp[i])
                i += 1
            else:
                keys.append(elements[element])

        filename_tmp = '{}_{}_{}_{}_{}_{}'.format(keys[0], keys[1], keys[2], keys[3], keys[4], keys[5]) # Root filename
        nested_sampler_path = os.path.join(input_path,  file, 'Nested_sampler')                         # Nested Sampler directory path

        # Samples
        filename            = filename_tmp + '.h5'
        input_filename      = os.path.join(nested_sampler_path, 'raynest.h5')
        output_filename     = os.path.join(output_path, filename)

        # Evidences
        filename_evidence   = filename_tmp + '_noise.txt'
        input_evidence      = os.path.join(nested_sampler_path, 'Evidence.txt')
        output_evidence     = os.path.join(output_evidence_dir, filename_evidence)

        # SNR
        filename_SNR        = filename_tmp + '_SNR.dat'
        input_SNR           = os.path.join(nested_sampler_path, 'optimal_SNR_TD.dat')
        output_SNR          = os.path.join(output_SNR_dir, filename_SNR)

        os.system('scp -r {input_filename} {output_filename}'.format(input_filename = input_filename, output_filename = output_filename))
        os.system('scp -r {input_evidence} {output_evidence}'.format(input_evidence = input_evidence, output_evidence = output_evidence))
        os.system('scp -r {input_SNR} {output_SNR}'.format(               input_SNR = input_SNR,           output_SNR = output_SNR))

print('Finished.')
