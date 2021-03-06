#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Net
%define		pnam	ICQ
Summary:	Net::ICQ perl module
Summary(pl.UTF-8):	Moduł perla Net::ICQ
Name:		perl-Net-ICQ
Version:	0.16
Release:	8
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0fd10c3daa3aa6e406f0bee4ba22a994
URL:		http://search.cpan.org/dist/Net-ICQ/
BuildRequires:	perl-Text-LineEditor
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Text-LineEditor
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::ICQ - simple ICQ client in Perl.

%description -l pl.UTF-8
Net::ICQ - prosty klient ICQ.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README* test*.pl
%{perl_vendorlib}/Net/ICQ.pm
%{_mandir}/man3/*
