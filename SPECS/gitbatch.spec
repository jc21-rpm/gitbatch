%define debug_package %{nil}

%global gh_user  isacikgoz

Name:           gitbatch
Version:        0.6.1
Release:        1
Summary:        Manage your git repositories in one place
Group:          Applications/System
License:        MIT
URL:            https://github.com/%{gh_user}/%{name}
Source:         https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
BuildRequires:  git golang

%description
Managing multiple git repositories is easier than ever. I (was) often end up working on
many directories and manually pulling updates etc. To make this routine faster, I created
a simple tool to handle this job. Although the focus is batch jobs, you can still do de
facto micro management of your git repositories (e.g add/reset, stash, commit etc.)

%prep
%setup -q -n %{name}-%{version}

%build
go build -o %{_builddir}/bin/%{name} cmd/gitbatch/main.go

%install
install -Dm0755 %{_builddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Mon Apr 19 2021 Jamie Curnow <jc@jc21.com> 0.6.1-1
- https://github.com/isacikgoz/gitbatch/releases/tag/v0.6.1

* Tue Nov 11 2019 Jamie Curnow <jc@jc21.com> 0.5.0-1
- Initial Spec
