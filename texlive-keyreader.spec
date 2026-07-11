%global tl_name keyreader
%global tl_revision 28195

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5b
Release:	%{tl_revision}.1
Summary:	A robust interface to xkeyval
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/keyreader
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/keyreader.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/keyreader.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a robust interface to controlling keys in xkeyval,
removing some of that package's restrictions. The package also addresses
some of the issues now covered by the author's ltxkeys package, which
was assumed to be a replacement for keyreader. Since keyreader has
remained a favourite with users, it has been reinstated.

