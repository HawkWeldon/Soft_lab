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
                        (pkgs.python313.withPackages (ps: with ps;[  ps.pypdf2
                                                                      ps.openpyxl
                                                                      ps.pypdf2
                                                                      ps.pyttsx3
                                                                      ps.flask  ]
                                                                                ))
                                                                                  ];
  LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [pkgs.espeak-ng];
}
