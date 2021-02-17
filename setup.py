import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


def main():
    install_list = []
    setuptools.setup(
        name="add_comments",
        version="0.0.1",
        author="RohitChattopadhyay",
        author_email="rohit.chattopadhyay1@gmail.com",
        description="Add Signature to your source code",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/RohitChattopadhyay/AddComments",
        packages=setuptools.find_packages(),
        install_requires=install_list,        
        license ='MIT', 
        entry_points ={ 
            'console_scripts': [ 
                'addcomments = add_comments.module:handler'
            ] 
        },
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.6',
    )


if __name__ == '__main__':
    main()