Summary:	Unifdef tool for removing ifdef'd lines
Summary(pl):	Narz�dzie unifdef do usuwania linii oznaczonych ifdef
Name:		unifdef
Version:	1.0
Release:	0.1
License:	BSD
Group:		Development/Languages
#Source0:	http://www.cs.cmu.edu/~ajw/dist/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	825240622f35c7b002f11ece1af4ba22
Patch0:		%{name}-codecleanup.diff
Source1:	%{name}-Makefile.am
Source2:	%{name}-configure.ac
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unifdef is useful for removing ifdefed lines from a file while
otherwise leaving the file alone. Unifdef acts on '#ifdef', '#ifndef',
'#else', and '#endif' lines, and it knows only enough about C and C++
to know when one of these is inactive because it is inside a comment,
or a single or double quote.

%description -l pl
unifdef jest przydatny do usuwania linii oznaczonych ifdef z pliku
pozostawiaj�c reszt� pliku w spokoju. unifdef dzia�a na liniach
'#ifdef', '#ifndef', '#else' i '#endif' i wie o C i C++ tylko tyle,
�eby odr�ni�, kiedy kt�ra� z tych dyrektyw jest nieaktywna, poniewa�
jest wewn�trz komentarza lub cudzys�ow�w.

%prep
%setup -q
rm -f Makefile unifdef *.o
cp %{SOURCE1} Makefile.am
cp %{SOURCE2} configure.ac
%patch0

%build
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/unifdef
%{_mandir}/man1/unifdef.1*
