{
  description = "1st-year UofT course grader's flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
          config = {
            allowUnfree = true;
          };
        };
        caugetch = pkgs.python311Packages.buildPythonPackage rec {
          pname = "caugetch";
          version = "0.0.1";
          #format = "wheel";

          src = pkgs.fetchFromGitHub {
            owner = "joeyespo";
            repo = "py-getch";
            rev = "24a625f24fbdc2d333db3d8a6f1b25071b2b16ae";
            hash = "sha256-FvpemQDIHTQglDx2Nl2AwQhzwRyW+VX7022IcvjRWCg=";
          };
        };
        getpass4 = pkgs.python311Packages.buildPythonPackage rec {
          pname = "getpass4";
          version = "0.0.14.1";
          #format = "wheel";
          src = pkgs.python311Packages.fetchPypi{
            inherit pname version;
            sha256 = "sha256-gKpOOmZfLszGzaPuIhJe61xjOOkcQMT9AQs8lMeqTTo=";
          };
          buildInputs = [ caugetch ];
          postPatch = ''
            sed -i 's/import caugetch/import getch/g' getpass4/*.py
            echo "Placeholder LICENSE" > LICENSE
          '';
        };

        python = pkgs.python311Packages.python;
        pythonEnv = python.withPackages (ps: with ps; [
          pandas
          numpy
          openpyxl
          configparser
          selenium
          getpass4
          caugetch

          #csv
          #scipy
          #jupyterlab  # Include JupyterLab in pythonEnv
          #ipykernel   # Include ipykernel to register kernels        
        ]);
      in
      {
        devShell = pkgs.mkShell {
          buildInputs = with pkgs; [
            pythonEnv
            firefox
            google-chrome
          ];
          shellHook = ''
          echo "Welcome to PHY Pod Grader!"
		  echo "Change the config file from sample_config.txt to whatever you want"
		  echo "Edit the grading scheme in Grading_Schemes.py"
		  echo "And run Marking.py to perform the grading and upload (if you set output to csv)"
          '';
        };
      }
    );
}
