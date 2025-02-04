%define upstream_name Proc-ProcessTable
%define upstream_version 0.59

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
Summary:	Interface to process table information

License:	GPL or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Proc/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel

%description
This module is a first crack at providing a consistent interface to
Unix (and maybe other multitasking OS's) process table information.
The impetus for this came about with my frustration at having to parse
the output of various systems' ps commands to check whether specific
processes were running on different boxes at a larged mixed Unix site.
The output format of ps was different on each OS, and sometimes
changed with each new release of an OS. Also, running a ps subprocess
from within a perl or shell script and parsing the output was not a
very efficient or aesthetic way to do things.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc README README.linux Changes contrib
%{perl_vendorarch}/Proc
%{perl_vendorarch}/auto/Proc
%{_mandir}/*/*
