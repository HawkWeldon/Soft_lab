{ pkgs ? import <nixpkgs> {
    config.permittedInsecurePackages = [
      "python3.13-pypdf2-3.0.1"
    ];
  }
}:

pkgs.mkShell 
{
  packages = with pkgs;[
                        espeak-ng 
                        (pkgs.python313.withPackages (ps: with ps;[   pypdf2
                                                                      openpyxl
                                                                      pypdf2
                                                                      pyttsx3
                                                                      flask  ]
                                                                                ))
                                                                                  ];
  LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [pkgs.espeak-ng];
}
