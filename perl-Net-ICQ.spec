%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	ICQ
Summary:	Net::ICQ perl module
Summary(pl):	Modu³ perla Net::ICQ
Name:		perl-Net-ICQ
Version:	0.16
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Text-LineEditor
Requires:	perl-Text-LineEditor
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::ICQ - simple ICQ client in Perl.

%description -l pl
Net::ICQ - prosty klient ICQ.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README* test*.pl
%{perl_sitelib}/Net/ICQ.pm
%{_mandir}/man3/*
